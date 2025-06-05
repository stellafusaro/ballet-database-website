$(document).ready(function() {
  $("#searchForm").submit(function(event) {
    event.preventDefault(); // Prevent default form submission

    var query = $("#searchInput").val().trim(); // Get user input and remove leading/trailing whitespace

    if (!query) {
      // If the input is empty or just whitespace, send a request to the backend to return 204 No Content
      fetch(window.location.pathname, { method: "POST" }).then(() => {
        $("#searchInput").val(""); // Clear the input
      });
    } else {
      // If there is a valid query, proceed to search results
      window.location.href = "/search?query=" + encodeURIComponent(query);
    }
  });
});

