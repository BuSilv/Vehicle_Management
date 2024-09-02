function changePage(choice) {
    var forms = document.querySelectorAll('.form-section');
    forms.forEach(form => {
        form.style.display = 'none';
    });

    var selectedForm = document.getElementById(choice + '_form');
    if (selectedForm) {
        selectedForm.style.display = 'block';
    }
}

function verifyvehicle(operation){
    
    var formContent = document.getElementById(operation + '_content');
    if (formContent) {
        formContent.style.display = 'block';
    }

    var verifySection = document.getElementById('button_' + operation + '_verify');
    if (verifySection) {
        verifySection.style.display = 'none';
    }

    document.getElementById(operation + '_placa').setAttribute('readonly', true);

    if (operation == 'consulta') {
        readVehicle()
    }

    if (operation == 'exclusao') {
        deleteVehicle()
    }

}

function readVehicle(){    

}

function deleteVehicle(){
    
}

function verifyvehicle(operation) {
    var placa = document.getElementById(operation + '_placa').value;
    var url = `/verificar_cadastro_veiculo?placa=${placa}`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            var formContent = document.getElementById(operation + '_content');
            if (formContent) {
                formContent.style.display = 'block';
            }

            var verifySection = document.getElementById('button_' + operation + '_verify');
            if (verifySection) {
                verifySection.style.display = 'none';
            }

            document.getElementById(operation + '_placa').setAttribute('readonly', true);

            if (operation === 'consulta') {
                // Exibir dados do veículo
                console.log(data);
            }

            if (operation === 'exclusao') {
                // Lógica para exclusão
            }
        })
        .catch(error => console.error('Erro:', error));
}
