var control_valor;
var singleValue;

$(document).ready(function(){
     control_valor=setInterval(refresh,1000);
       $('#update').click(function() {
          //alert('clicked');
          var singleValue = $( "#selection" ).val();
          clearInterval(control_valor);
          control_valor=setInterval(refresh,(singleValue*1000).toString());
          this.value = singleValue.toString();
      });
});


function refresh() {
        $.get("/valores",function(data){
          $("#Temperatura").html("Temperatura [%]: " + data.temperatura.toString());
          $("#Humedad").html("Humedad [%]: " + data.humedad.toString());
          $("#Presatm").html("PA [hPa]: " + data.presatm.toString());
          $("#Velviento").html("Velocidad de viento [km/h]: " + data.velviento.toString());
          $("#lastTemperatura").html("Temperatura [°C]: " + data.lasttemperatura.toString());
          $("#lastHumedad").html("Humedad [%]: " + data.lasthumedad.toString());
          $("#lastPresatm").html("PA [hPa]: " + data.lastpresatm.toString());
          $("#lastVelviento").html("Velocidad de viento [km/h]: " + data.lastvelviento.toString());
        });
}