// Replace 'YOUR_API_KEY' with your actual API key (api_...).
const pageclipAPIKey = 'api_GrjsXdYCWwLTzIQwDPkrziH9IF9YvQw0';
const formName = 'Amzn';
const pageclipEndpoint = `https://api.pageclip.co/data/${formName}`;

// Fetch data from the "amzn" form.
fetch(pageclipEndpoint, {
  method: 'GET',
  headers: {
    'Accept': 'application/vnd.pageclip.v1+json',
    'Authorization': `Basic ${btoa(pageclipAPIKey + ':')}`,
  },
})
  .then(response => response.json())
  .then(data => {
    // 'data' variable contains the fetched data from the "amzn" form.
    // Assuming the data is in an array format, you can iterate through it to access individual entries.
    data.data.forEach(item => {
      const name = item.payload.name;
      const gmail = item.payload.email;
      const amazonLink = item.payload.amazonLink;
      const number = item.payload.phoneNumber;

      // Do something with the retrieved data (e.g., display it on the web page or process it further).
      console.log('Name:', name);
      console.log('Gmail:', gmail);
      console.log('Amazon Link:', amazonLink);
      console.log('Number:', number);
    });
  })
  .catch(error => {
    // Handle any errors that occurred during the API request.
    console.error('Error fetching data:', error);
  });



