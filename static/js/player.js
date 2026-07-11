const params =
    new URLSearchParams(
        window.location.search
    );

const videoId =
    params.get(
        "videoId"
    );

async function loadSong(){

    const response =
        await fetch(
            `/song/${videoId}`
        );

    const data =
        await response.json();

    document
        .getElementById(
            "thumbnail"
        )
        .src =
        data.thumbnail;

    document
        .getElementById(
            "title"
        )
        .innerText =
        data.title;

    document
        .getElementById(
            "artist"
        )
        .innerText =
        data.artist;

    const player =
        document
        .getElementById(
            "player"
        );

    player.src =
        data.audioUrl;

    player.play();
}

async function loadRecommendations(){

    const response =
        await fetch(
            `/recommend/${videoId}`
        );

    const songs =
        await response.json();

    const container =
        document
        .getElementById(
            "recommendations"
        );

    container.innerHTML = "";

    songs.forEach(song => {

        container.innerHTML += `

        <div

            class="recommendation"

            onclick="
                location.href=
                '/player?videoId=${song.videoId}'
            ">

            <img
                src="${song.thumbnail}">

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

loadSong();

loadRecommendations();