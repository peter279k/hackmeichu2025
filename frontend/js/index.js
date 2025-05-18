async function fetchElectricCarbonFactor() {
    jsonUrl = 'http://localhost:8000/api/v1/electric_carbon_factor';
    await $.ajax({
        url: jsonUrl,
                method: 'GET',
                headers: {'Accept': 'application/json'},
            }).done((data) => {
                console.log(JSON.parse(data));
            });
}
