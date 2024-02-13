const $recForm = document.forms.recommendation
const $recommendationTextarea = document.getElementById('recommendation')
const $checkboxes = document.querySelectorAll('.genre')


$recForm.addEventListener('submit',  (e) => {
    console.log(e, 'event')
    e.preventDefault()

    let genres = null
    $checkboxes.forEach(el => {


        console.log( el, 'hghg')
        if (el.checked) {

            genres.push(el.value)
        }
    })

    // if (!currentRating) return

    // try {
    //     const currentUrl = window.location.href;
    //     const crf_token = document.getElementsByName('csrfmiddlewaretoken')[0].getAttribute('value');
    //     await fetch(`${currentUrl}review-create/`, {
    //         method: 'POST',
    //         headers: {
    //             'Content-Type': 'application/json',
    //             'X-CSRFToken': crf_token
    //         },
    //         body: JSON.stringify({
    //             'rating': currentRating,
    //             'text': reviewValue,
    //             'user_id': userData
    //         }),
    //     });
    //     setTimeout(() => {
    //         window.location.reload()
    //     }, 1000);
    //
    // } catch (error) {
    //     alert(error);
    // }


})