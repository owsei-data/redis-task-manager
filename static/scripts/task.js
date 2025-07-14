function criarTarefa() {
  const titulo = document.getElementById('titulo').value;
  const descricao = document.getElementById('descricao').value;
  const deadline = document.getElementById('deadline').value;

  fetch('/criar-tarefa', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      titulo: titulo,
      descricao: descricao,
      deadline: deadline
    })
  })
  .then(response => response.json())
  .then(data => {
    alert("Tarefa criada com sucesso! ID: " + data.id);
    window.location.reload();
  })
  .catch(error => {
    console.error('Erro:', error);
    alert("Erro ao criar tarefa.");
  });
}
function mostrarFormulario() {
  const form = document.getElementById('formulario-tarefa');
  if (form.style.display === 'none') {
    form.style.display = 'block';
  } else {
    form.style.display = 'none';
  }
}

