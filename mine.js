fetch('resume.json')
  .then(response => response.json())
  .then(data => {
    console.log(data); // Just logs the JSON data in your browser console for now

    // Example: display your name from the JSON in an element with id="name"
    document.getElementById('name').textContent = data.name;
  })
  .catch(error => console.error('Error loading JSON:', error));
