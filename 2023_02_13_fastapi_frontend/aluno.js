console.log("Rodando arquivo JS")

var api_url = 'http://localhost:8000/api/v1/alunos';

lista_selecionada = false

    function get_alunos(){

        fetch(api_url)


        .then(Response => Response.text())

        .then(text => {
                console.log(text)

                let dados = JSON.parse(text)
                console.log(dados)

                let tbody = document.getElementById('tbody-pessoas')

                tbody.innerHTML = ""

                dados.forEach(aluno => {
                    tbody.innerHTML += `
                                        <tr>
                                            <td>${aluno.id}</td>
                                            <td>${aluno.nome}</td>
                                            <td>${aluno.email}</td>
                                            <td>
                                            <a href="save_aluno.html?id=${aluno.id}">editar</a> |
                                            <button onclick='remove_aluno(${aluno.id})'>deletar</button>
                                            </td>
                                 
                                         </tr>
                                         `
                    
                });
            }
        )

        lista_selecionada = "alunos"

}


    function get_aluno(){
        let id = document.getElementById("id_busca").value


        fetch(`http://127.0.0.1:8000/api/v1/alunos/${id}`,
            {
                Headers:
                {
                    'Accept': 'aplication/json'
                }
            }
        )

        .then(Response => Response.text())

        .then(text => {
                console.log(text)

                let aluno = JSON.parse(text)
                console.log(aluno)

                let tbody = document.getElementById('tbody-pessoas')

                tbody.innerHTML = "";
                tbody.innerHTML += `
                                        <tr>
                                            <td>${aluno.id}</td>
                                            <td>${aluno.nome}</td>
                                            <td>${aluno.email}</td>
                                            <td>
                                            <a href="save_aluno.html?id=${aluno.id}">editar</a> |
                                            <button onclick='remove_aluno(${aluno.id})'>deletar</button>
                                            </td>                                 
                                        </tr>
                              
                                         `
            }
        )

    }



function get_professores(){

    fetch(
        'http://127.0.0.1:8000/api/v1/professores/',
        {
            Headers:
            {
                'Accept': 'aplication/json'
            }
        }
    )


    .then(Response => Response.text())

    .then(text => {
        console.log(text)

        let dados = JSON.parse(text)
        console.log(dados)

        let tbody = document.getElementById('tbody-pessoas')
        
        tbody.innerHTML = ""
        dados.forEach(professor => {
            tbody.innerHTML += `
                                <tr>
                                    <td>${professor.id}</td>
                                    <td>${professor.nome}</td>
                                    <td>${professor.email}</td>
                                    <td>
                                    <a href="save_professor.html?id=${professor.id}">editar</a> |
                                    <button onclick='remove_professor(${professor.id})'>deletar</button>
                                    </td>                                 

                                 </tr>
                                 `
            
        });
    })
    lista_selecionada = "professores"

}

function get_professor(){
    let id = document.getElementById("id_busca").value


    fetch(`http://127.0.0.1:8000/api/v1/professores/${id}`,
        {
            Headers:
            {
                'Accept': 'aplication/json'
            }
        }
    )

    .then(Response => Response.text())

    .then(text => {
            console.log(text)

            let dados = JSON.parse(text)
            console.log(dados)

            let tbody = document.getElementById('tbody-pessoas')

            tbody.innerHTML = "";

            tbody.innerHTML += `
                                    <tr>
                                        <td>${dados.id}</td>
                                        <td>${dados.nome}</td>
                                        <td>${dados.email}</td>
                                        <td>
                                        <a href="save_professor.html?id=${dados.id}">editar</a> |
                                        <button onclick='remove_professor(${dados.id})'>deletar</button>
                                        </td>                                 
                                     </tr>
                                     `
        }
    )

}

function get_usuarios(){

    fetch(
        'http://127.0.0.1:8000/api/v1/usuarios/',
        {
            Headers:
            {
                'Accept': 'aplication/json'
            }
        }
    )


    .then(Response => Response.text())

    .then(text => {
        console.log(text)

        let dados = JSON.parse(text)
        console.log(dados)

        let tbody = document.getElementById('tbody-pessoas')
        
        tbody.innerHTML = ""
        dados.forEach(usuario => {
            tbody.innerHTML += `
                                <tr>
                                    <td>${usuario.id}</td>
                                    <td>${usuario.nome}</td>
                                    <td>${usuario.email}</td>
                                    <td>
                                    <a href="save_usuario.html?id=${usuario.id}">editar</a> |
                                    <button onclick='remove_usuario(${usuario.id})'>deletar</button>
                                    </td>                                 
                                 </tr>
                                 `
            
        });
    })

    lista_selecionada = "usuarios"


}

function get_usuario(){
    let id = document.getElementById("id_busca").value


    fetch(`http://127.0.0.1:8000/api/v1/usuarios/${id}`,
        {
            Headers:
            {
                'Accept': 'aplication/json'
            }
        }
    )

    .then(Response => Response.text())

    .then(text => {
            console.log(text)

            let dados = JSON.parse(text)
            console.log(dados)

            let tbody = document.getElementById('tbody-pessoas')

            tbody.innerHTML = "";

            tbody.innerHTML += `
                                    <tr>
                                        <td>${dados.id}</td>
                                        <td>${dados.nome}</td>
                                        <td>${dados.email}</td>
                                        <td>
                                        <a href="save_usuario.html?id=${dados.id}">editar</a> |
                                        <button onclick='remove_usuario(${dados.id})'>deletar</button>
                                        </td>                                 
                                     </tr>
                                     `
        }
    )

}

function filtrar_busca(){
    if (lista_selecionada == "alunos"){
        get_aluno()
    }
    else if (lista_selecionada == "professores"){
        get_professor()
    }
    else {
        get_usuario()
    }
}


function remove_aluno(id){
    fetch(`${api_url}/${id}`,{
        method: 'DELETE',
        headers: {
            'Accept': 'application/json'
        }
    })
    .then(response => {
        if(response.status == 204){
            get_alunos();
        }else{
            alert("Erro");
        }
    })
 }

 function remove_professor(id){
    fetch(`http://127.0.0.1:8000/api/v1/professores/${id}`,{
        method: 'DELETE',
        headers: {
            'Accept': 'application/json'
        }
    })
    .then(response => {
        if(response.status == 204){
            get_alunos();
        }else{
            alert("Erro");
        }
    })
 }

 function remove_usuario(id){
    fetch(`http://127.0.0.1:8000/api/v1/usuarios/${id}`,{
        method: 'DELETE',
        headers: {
            'Accept': 'application/json'
        }
    })
    .then(response => {
        if(response.status == 204){
            get_alunos();
        }else{
            alert("Erro");
        }
    })
 }


 function get_by_id(id_aluno){
    let aluno = fetch(`${api_url}/${id_aluno}`)
    .then(response => response.text())
    .then(function(text) {    
      return JSON.parse(text);
    });   
    return aluno;
 }
 
 
 function load_aluno(id_aluno){
    get_by_id(id_aluno).then(aluno =>{
        console.log(document.getElementById("id").value = aluno.id)
        console.log(document.getElementById("nome").value = aluno.nome)
        console.log(document.getElementById("email").value = aluno.email)
    });
  
 } 

 function save(){
    let id = document.getElementById("id").value;
    let nome = document.getElementById("nome").value;
    let email = document.getElementById("email").value;
       
    if(id != ''){
        console.log('editar')
        aluno = {"id":id, "nome": nome, "email": email}
        update(aluno);
    }
    else{
        aluno = {"nome": nome, "email": email}
        create(aluno);
    }       
}
 
 
function update(aluno){
    let mensagem = document.getElementById("mensagem");
    fetch(`${api_url}/${aluno.id}`,{
        method: 'PUT',
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
        },
        body: JSON.stringify(aluno)
    })

    .then(response => {
        if(response.status == 202){
            mensagem.innerHTML = "Alterado com sucesso";
        }else{
            mensagem.innerHTML = "Erro";
        }
    })
}