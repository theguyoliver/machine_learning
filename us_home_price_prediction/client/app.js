// Function to handle prediction
function onClickedEstimatePrice() {
    console.log("Predict button clicked");

    // Collecting form data
    const n_bedrooms = parseInt(document.getElementById("bedrooms").value);
    const n_bathrooms = parseInt(document.getElementById("bathrooms").value);
    const sqft_living = parseInt(document.getElementById("livingSpace").value);
    const sqft_lot = parseInt(document.getElementById("lotSize").value);
    const floors = parseInt(document.querySelector('input[name="floors"]:checked')?.value);
    const yrs_since_last_renovation = parseInt(document.getElementById("renovation").value);
    const basement = document.getElementById("basement").value.toLowerCase();
    const city = document.getElementById("city").value;

    // Ensure all fields are filled
    if (isNaN(n_bedrooms) || isNaN(n_bathrooms) || isNaN(sqft_living) || isNaN(sqft_lot) || isNaN(floors) || isNaN(yrs_since_last_renovation) || basement === "" || city === "") {
        alert("Please fill out all fields correctly.");
        return;
    }

    // Payload to send to the server
    const data = {
        n_bedrooms,
        n_bathrooms,
        sqft_living,
        sqft_lot,
        floors,
        yrs_since_last_renovation,
        basement,
        city
    };

    console.log("Payload:", data);

    // Make a POST request to the server
    $.post("http://127.0.0.1:5000/get_estimated_price", data, function(response) {
        console.log("Response:", response);
        // Display the prediction result
        document.getElementById("predictionOutput").innerHTML =
            `<h2>Estimated Price: $${response.estimated_price}</h2>`;
    }).fail(function(error) {
        console.error("Error occurred:", error);
        alert("Failed to get prediction. Please try again.");
    });
}

// Attach the event listener to the button
document.getElementById("predictButton").addEventListener("click", onClickedEstimatePrice);
