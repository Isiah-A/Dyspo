const API_URL = `http://localhost:8080`;

function fetchData() {
   fetch(`${API_URL}/moods`)
        .then(res => res.json())
        .then(data => {
            show(data);
        })
        .catch(error => {
            console.error(`Error Fetching entries: ${error}`);
            document.getElementById('entries-list').innerHTML = 'Error Loading Entries';

        });
}

// takes a UNIX integer date, and produces a prettier human string
//function dateOf(date) {
//  const milliseconds = date * 1000; // 1575909015000
//  const dateObject = new Date(milliseconds);
//  const humanDateFormat = dateObject.toLocaleString(); //2019-12-9 10:30:15
//  return humanDateFormat;
//}

function show(data) {
  // the data parameter will be a JS array of JS objects
  // this uses a combination of "HTML building" DOM methods (the document createElements) and
  // simple string interpolation (see the 'a' tag on title)
  // both are valid ways of building the html.
  const entriesListDiv = document.getElementById('entries-list');
  const list = document.createDocumentFragment();
//  console.log('Data:', data);

  data.map(function (entry) {
     let li = document.createElement('li');
        let title = document.createElement('h3');
        title.innerHTML = `${entry.name}`;

        let rating = document.createElement('p');
        rating.textContent = `Rating ${entry.rating}`;

        let notes = document.createElement('p');
        notes.textContent = `Notes: ${entry.notes}`;
        notes.style.fontStyle = 'italic';

        let timestamp = document.createElement('small');
        const dateObject = new Date(entry.timestamp);
        timestamp.textContent = `Logged: ${dateObject.toLocaleString()}`;
        timestamp.style.display = 'block';
        timestamp.style.color = '#666';


        li.appendChild(title);
        li.appendChild(rating);
        li.appendChild(notes);
        li.appendChild(timestamp);
        list.appendChild(li);


      });

        entriesListDiv.appendChild(list);
}

function handlePage() {
    console.log('load all moods');
    fetchData();
}

handlePage();

//const API_URL = `http://localhost:8080`;
//
//function fetchEntriesData() {
//    fetch(`${API_URL}/moods`)
//        .then(res => res.json())
//        .then(data => {
//            showEntryList(data);
//        })
//        .catch(error => {
//            console.error(`Error Fetching entries: ${error}`);
//            document.getElementById('entries-list').innerHTML = 'Error Loading Entries';
//        });
//}
//
//function showEntryList(data) {
//    const entriesListDiv = document.getElementById('entries-list');
//    const list = document.createDocumentFragment();
//
//    data.map(function (entry) {
//        let div = document.createElement('div');
//        let title = document.createElement('h3');
//        title.textContent = entry.name;
//
//        let details = document.createElement('p');
//        details.textContent = `Rating ${entry.rating}`;
////
////        let imdbLink = document.createElement('a');
////        imdbLink.href = `${entry.link}`;
////        imdbLink.textContent = 'IMDb Link';
////
////        let genres = document.createElement('p');
////        genres.textContent = `Genres: ${entry.genres.join(', ')}`;
//
//        let viewLink = document.createElement('a');
//        viewLink.href = `/ui/entry_detail.html?entryid=${entry.id}`;
//        viewLink.textContent = 'View Details';
//
//        div.appendChild(title);
////        div.appendChild(details);
////        div.appendChild(imdbLink);
////        div.appendChild(genres);
////        div.appendChild(viewLink);
//
//        list.appendChild(div);
//    });
//
//    entriesListDiv.appendChild(list);
//}
//
//function handlePage() {
//    console.log('load all entries');
//    fetchEntriesData();
//}
//
//handlePage();
