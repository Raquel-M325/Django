function comenteiAqui(numero){
    const form = document.getElementById("form-comentario-" + numero)
    const autor = form.querySelector("[name='autor']").value
    const conteudo = form.querySelector("[name='conteudo']").value

    fetch("/comentarios/comentario/", {
        method: "POST",
        body: new URLSearchParams({ autor: autor, conteudo: conteudo }),
        headers: { "X-CSRFToken": form.querySelector("[name='csrfmiddlewaretoken']").value }
    })
    .then(res => res.json())
    .then(data => {
        // pegará o ok com numero de postagens e mostrará depois que clicou no botao 
        document.getElementById("ok-" + numero).style.display = "block"

        // e mostrará a mensagem de confirmacao
        document.getElementById("ok-" + numero).innerHTML = data.ok

        // pegara o resultado para mostrar o comentario
        document.getElementById("resultado-" + numero).style.display = "block"

        // mostrar o resultado com as informacoes que foi comentado com formato do li
        document.getElementById("comentou-" + numero).innerHTML += "<li>" + data.completo + "</li>"
    })
}