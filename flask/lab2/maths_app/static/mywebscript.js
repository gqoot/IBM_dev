let runAddition = () => {
    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);

    let result = num1 + num2;
    document.getElementById("system_response").innerHTML = "Result: " + result;
};

let runSubtraction = () => {
    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);

    let result = num1 - num2;
    document.getElementById("system_response").innerHTML = "Result: " + result;
};

let runMultiplication = () => {
    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);

    let result = num1 * num2;
    document.getElementById("system_response").innerHTML = "Result: " + result;
};

async function performOperation(operation) {
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;
    const response = await fetch(`https://gaurav4rana-8000.theiadockernext-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/${operation}?num1=${num1}&num2=${num2}`);
    const res = await response.json();
    const result = res['result'];
    document.getElementById('system_response').innerText = `Result : ${result}`;
}