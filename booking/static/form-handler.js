document.getElementById('search_form').addEventListener('submit', function(e){
    e.preventDefault();  // Prevent form submission

    const formData = new FormData(e.target);
    var origin = formData.get('origin');
    var destination = formData.get('destination');
    var to_date = new Date(formData.get('to_date'));
    var from_date = new Date(formData.get('from_date'));

    console.log(origin);
    console.log(destination);
    console.log(to_date);
    console.log(from_date);

    // Reset custom validity before new validation
    document.getElementById('origin').setCustomValidity('');
    document.getElementById('destination').setCustomValidity('');
    document.getElementById('from_date').setCustomValidity('');
    document.getElementById('to_date').setCustomValidity('');

    // Perform validation
    if (origin == destination) {
        const destinationE1 = document.getElementById('destination')
        destinationE1.setCustomValidity('Origin and Destination must be different!');
        destinationE1.reportValidity();

    }

    if (to_date < from_date) {
        const fromDateE1 = document.getElementById('from_date')
        fromDateE1.setCustomValidity('Date range invalid. From date must be before To date!');
        fromDateE1.reportValidity();
    }

      // If the form is valid, submit it
    if (document.querySelector('form').checkValidity()) {
        e.target.submit();  // Submit the form
    }
});

// Clear custom validity when user changes the input
document.getElementById('origin').addEventListener('change', function() {
    this.setCustomValidity('');
});
document.getElementById('destination').addEventListener('change', function() {
    this.setCustomValidity('');
});
document.getElementById('from_date').addEventListener('input', function() {
    this.setCustomValidity('');
});
document.getElementById('to_date').addEventListener('input', function() {
    this.setCustomValidity('');
});



// Function to ensure destination is North Shore Airport when origin is not Dairy Flat (NZNE)
function validateNorthShoreDestinationLogic(){

  const origin = document.getElementById('origin').value;
  const destination = document.getElementById('destination');

  if(origin !== 'NZNE' && destination.value != 'NZNE'){

    destination.setCustomValidity('There are only flights to North Shore Airport from this origin.');
    destination.reportValidity();
     }
    else {
    destination.setCustomValidity('');
  }
}



document.getElementById('origin').addEventListener('change', function(e) {
  const origin = e.target.value;
  const  destination = document.getElementById('destination');
  console.log(origin);
  console.log(destination.value)

  if (origin != 'NZNE' &&  destination.value != 'NZNE' ) {
    destination.setCustomValidity('There are only flights to NorthShore Airport from this origin. Select North Shore Airport');
    destination.reportValidity();

  }else{
  destination.setCustomValidity('');
  }
});

document.getElementById('origin').addEventListener('change', validateNorthShoreDestinationLogic);
document.getElementById('destination').addEventListener('change', validateNorthShoreDestinationLogic);