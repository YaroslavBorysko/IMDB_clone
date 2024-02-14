const $recForm = document.forms.recommendation
const $recommendationTextarea = document.getElementById('recommendation')
const $checkboxes = document.querySelectorAll('.genre')
const $fromSelect = document.getElementById('from')
const $toSelect = document.getElementById('to')

let recommendationValue = ''
let from = ''
let to = ''
const submitBtn = document.querySelector('.send-comment')


let response = null
$recommendationTextarea.addEventListener('change', (e) => {
    recommendationValue = e.target.value
})

$fromSelect.addEventListener('change', (e) => {
    from = e.target.value
})

$toSelect.addEventListener('change', (e) => {
    to = e.target.value
})

$recForm.addEventListener('submit',  (e) => {
    e.preventDefault()
    const $parent = document.getElementById('recommendations-page')
    const $prevFilm = document.querySelector('.film-wrapper')

    if($prevFilm) {
        $parent.removeChild($prevFilm)
    }

    let genres = []
    $checkboxes.forEach(el => {
        if (el.checked) {
            genres.push(el.value)
        }
    })

    try {
        const currentUrl = window.location.href;
        const crf_token = document.getElementsByName('csrfmiddlewaretoken')[0].getAttribute('value');
        submitBtn.innerHTML = "Loading..."
        fetch(currentUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': crf_token
            },
            body: JSON.stringify({
                genre: genres,
                end_date: to,
                start_date: from,
                description: recommendationValue
            })

        }).then(data => data.json())
            .then(data => {
                submitBtn.innerHTML = "Recommend again"
                console.log(data)
                if(data) {
                    console.log( 2)
                    const $parentContainer = document.getElementById('recommendations-page')
                    const $container = document.createElement('div')
                    const $poster = document.createElement('img')
                    const $title = document.createElement('h2')
                    const $description = document.createElement('p')
                    const $flexWrapper = document.createElement('div')
                    const $posterWrapper = document.createElement('div')
                    const $contentWrapper = document.createElement('div')

                    $container.classList.add('film-wrapper')

                    $posterWrapper.classList.add('film-poster__wrapper')
                    $contentWrapper.classList.add('film-content__wrapper')
                    $flexWrapper.classList.add('film-content__flex-wrapper')
                    $poster.classList.add('film-poster')
                    $poster.setAttribute('src',data.poster_url )
                    $poster.setAttribute('alt','poster')

                    $title.classList.add('film-title')
                    $title.innerHTML = data.title
                    $description.classList.add('film-plot')
                    $description.innerHTML = data.plot

                    $posterWrapper.append($poster)
                    $flexWrapper.append($posterWrapper)

                    $contentWrapper.append($title)
                    $contentWrapper.append($description)

                    $flexWrapper.append($contentWrapper)

                    $container.append($flexWrapper)
                    $parentContainer.append($container)
                }
            });

    } catch (error) {
        alert(error);
    }
})

