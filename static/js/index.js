
let offset = 0;

let currentQuery = "";

let loading = false;

async function searchSongs(){

    currentQuery =
        document.getElementById(
            "searchBox"
        ).value;

    offset = 0;

    const response =
        await fetch(
            `/search?query=${encodeURIComponent(
                currentQuery
            )}&offset=0`
        );

    const songs =
        await response.json();

    const results =
        document.getElementById(
            "results"
        );

    results.innerHTML = "";

    songs.forEach(song => {

        results.innerHTML += `

        <div
            class="song-card"

            onclick="
                location.href=
                '/player?videoId=${song.videoId}'
            ">

            <img
                class="thumbnail"

                src="${song.thumbnail}"

                onerror="
                    this.src=
                    '${song.fallbackThumbnail}'
                ">

            <div>

                <h3>
                    ${song.title}
                </h3>

                <p>
                    ${song.artist}
                </p>

            </div>

        </div>

        `;
    });
}

async function loadMoreSongs(){

    if(
        loading ||
        currentQuery === ""
    )
        return;

    loading = true;

    offset += 20;

    const response =
        await fetch(
            `/search?query=${encodeURIComponent(
                currentQuery
            )}&offset=${offset}`
        );

    const songs =
        await response.json();

    const results =
        document.getElementById(
            "results"
        );

    songs.forEach(song => {

        results.innerHTML += `

        <div
            class="song-card"

            onclick="
                location.href=
                '/player?videoId=${song.videoId}'
            ">

            <img
                class="thumbnail"

                src="${song.thumbnail}"

                onerror="
                    this.src=
                    '${song.fallbackThumbnail}'
                ">

            <div>

                <h3>
                    ${song.title}
                </h3>

                <p>
                    ${song.artist}
                </p>

            </div>

        </div>

        `;
    });

    loading = false;
}

window.addEventListener(
    "scroll",
    () => {

        if(

            window.innerHeight +
            window.scrollY

            >=

            document.body.offsetHeight - 200

        ){
            loadMoreSongs();
        }

    }
);

