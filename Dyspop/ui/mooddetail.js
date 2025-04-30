const API_URL = `http://localhost:8080`;

function fetchMood(entryId) {
  fetch(`${API_URL}/moods/${entryId}`)
    .then(res => {
      //console.log("res is ", Object.prototype.toString.call(res));
      return res.json();
    })
    .then(data => {
      showMoodDetail(data);
    })
    .catch(error => {
      console.log(`Error Fetching data : ${error}`);
      document.getElementById('Entry').innerHTML = 'Error Loading Single Mood Data';
    });
}

function parseEntryId() {
  try {
    var url_string = window.location.href.toLowerCase();
    var url = new URL(url_string);
    var entryId = url.searchParams.get('entryid');
    return entryId;
  } catch (err) {
    console.log("Issues with Parsing URL Parameter's - " + err);
    return '0';
  }
}
// takes a UNIX integer date, and produces a prettier human string
function dateOf(date) {
  const milliseconds = date * 1000; // 1575909015000
  const dateObject = new Date(milliseconds);
  const humanDateFormat = dateObject.toLocaleString(); //2019-12-9 10:30:15
  return humanDateFormat;
}

function showMoodDetail(entry) {
  // the data parameter will be a JS array of JS objects
  // this uses a combination of "HTML building" DOM methods (the document createElements) and
  // simple string interpolation (see the 'a' tag on title)
  // both are valid ways of building the html.
  const ul = document.getElementById('Entry');
  const detail = document.createDocumentFragment();

//  let viewlink = doucment.createElement('a');
//  viewlink.href = `/Dyspop/mooddetail.html?entryid=${entry.id}`;
//  viewlink.textContext = 'View Details';

  console.log('Mood Entry Data:', entry);
   // elements to display the mood details
  let li = document.createElement('li');
  let name = document.createElement('h2');
  let rating = document.createElement('p');
  let notes = document.createElement('p');
  let timestamp = document.createElement('p');

  const dateObject = new Date(entry.timestamp);
  name.textContent = entry.name;
  rating.textContent = `Rating: ${entry.rating}`;
  notes.textContent = `Notes: ${entry.notes}`;
  timestamp.textContent = `Logged: ${dateObject.toLocaleString()}`;
  timestamp.style.color = '#666';


  li.appendChild(name);
//  li.appendChild(viewlink);
  li.appendChild(rating);
  li.appendChild(notes);
  li.appendChild(timestamp)
  detail.appendChild(li);

  ul.appendChild(detail);
}

function handlePage() {
  let entryId = parseEntryId();
  console.log('Mood Entry ID:', entryId);

  if (entryId != null) {
    console.log('found an entryId');
    fetchMood(entryId);
  }
}

handlePage();
