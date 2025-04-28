// /Users/isiah/PycharmProjects/PassionProject/Dyspop/ui/moodcreate.js
const API_URL = `http://localhost:8080`;

// Handles the form submission event
function handleFormSubmit(event) {
  event.preventDefault(); // Prevent the default form submission which reloads the page

  // Get form data using the correct form ID
  const form = document.getElementById('addpiroform');
  const formData = new FormData(form);

  // Convert FormData to a plain JavaScript object
  const moodData = {};
  formData.forEach((value, key) => {
    // Ensure rating is stored as a number if needed, though backend handles int()
    moodData[key] = key === 'rating' ? parseInt(value, 10) : value;
  });

  console.log('Sending mood data:', moodData);

  // Convert the object to a JSON string
  const jsonPayload = JSON.stringify(moodData);

  // Call the function to POST the JSON data
  postMoodData(jsonPayload);
}

// Sends the JSON data to the backend API
async function postMoodData(jsonData) {
  try {
    // Correct API endpoint for creating moods
    const response = await fetch(`${API_URL}/moods`, {
      method: 'POST',
      headers: {
        // Let the browser set Content-Type for FormData if sending that directly,
        // but for JSON, we set it explicitly.
        'Content-Type': 'application/json',
        'Accept': 'application/json' // Indicate we expect JSON back
      },
      body: jsonData, // Send the JSON string as the body
    });

    // Check if the request was successful (status code 2xx)
    if (!response.ok) {
        // If not successful, try to parse error response from backend
        const errorData = await response.json().catch(() => ({ error: 'Unknown error occurred' }));
        throw new Error(`HTTP error! status: ${response.status}, message: ${errorData.error || 'Failed to add mood'}`);
    }

    const result = await response.json();
    console.log('Success:', result);
    alert('Mood added successfully!'); // Give user feedback
    // Optionally redirect or clear the form
    window.location.href = '/ui/moodlist.html'; // Redirect to the list page

  } catch (error) {
    console.error('Error posting mood:', error);
    alert(`Error adding mood: ${error.message}`); // Show error to user
  }
}

// Add event listener when the DOM is ready
window.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('addpiroform');
    if (form) {
      // Listen for the 'submit' event on the FORM, not a click on the button
      form.addEventListener('submit', handleFormSubmit);
      console.log('Form event listener attached.');
    } else {
      console.error('Form with ID "addpiroform" not found!');
    }
  },
  false,
);