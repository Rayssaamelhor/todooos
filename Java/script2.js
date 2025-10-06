function converterTemperatura(){
    let temperaturaCelsius = parseFloat(document.getElementById("temperaturaC").value);

    let temperaturaFahrenheit = (temperaturaCelsius*9/5)+32;

    alert(`A tenperatura em Fahrenheit é: ${temperaturaFahrenheit.toFixed(2)}`);
}