async function fetchElectricCarbonFactor() {
    let apiUrl = $('#api-endpoint').val();
    apiUrl = '/api/v1/electric_carbon_factor';
    await $.ajax({
        url: apiUrl,
        method: 'GET',
        headers: {'Accept': 'application/json'},
    }).done((data) => {
        console.log(JSON.parse(data));
    }).error(error) => {
        Swal.fire({
            'title': '錯誤',
            'text': error,
            'icon': 'error',
        });
    };
}

async function calculateElectricCarbonFactor() {

}
