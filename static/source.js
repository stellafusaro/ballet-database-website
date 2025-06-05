const popularBallets = [
	{
		id: "1",
                title: "Swan Lake",
                image: "https://www.metopera.org/globalassets/season/abt/2022-abt/swan-lake/slbrandtcornejo2ro_16    00x685.png"
	},
        {
        	id: "6",
                title: "Don Quixote",
               	image: "https://upload.wikimedia.org/wikipedia/commons/5/5d/Don_Quixote_Ballet.jpg"
        },
        {
        	id: "9",
                title: "Romeo and Juliet",
                image: "https://upload.wikimedia.org/wikipedia/commons/8/85/Romeo_and_Juliet_ballet.jpg"
        }
];
function loadPopularBallets() {
	const container = document.getElementById("popular-ballets");
        container.innerHTML = "";
              
        popularBallets.forEach(ballet => {
       		const balletDiv = document.createElement("div");
        	balletDiv.classList.add("ballet-item");
        	balletDiv.innerHTML = `
       		<img src="${ballet.image}" alt="${ballet.title}" />
        	<h2>${ballet.title}</h2>
        	<a href="/view/${ballet.id}">View Details</a>`;
		container.appendChild(balletDiv);
        });
}
          
document.addEventListener("DOMContentLoaded", loadPopularBallets);
