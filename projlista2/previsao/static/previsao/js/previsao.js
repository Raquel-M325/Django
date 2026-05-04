function buscarCidade(){
    const cidade = document.getElementById("cidade").value
    const resultado = document.getElementById("resultado")

    fetch("/previsao/cidade/?cidade=" + cidade)
    .then(res => res.json())
    .then(data => {
        if (data.erro){
            resultado.className = "box mt-4 has-background-danger-light"
            document.getElementById("resposta-erro").innerHTML = data.erro
            document.getElementById("lista-resultado").style.display = "none"

        } else {
            resultado.className = "box mt-4 has-background-success-light"
            document.getElementById("resposta-cidade").innerHTML = data.cidade
            document.getElementById("resposta-clima").innerHTML = data.clima
            document.getElementById("resposta-temperatura").innerHTML = data.temperatura
            document.getElementById("resposta-erro").innerHTML = ""
            document.getElementById("lista-resultado").style.display = "block"

        }

        resultado.style.display = "block"
    })
}