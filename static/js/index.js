$(document).ready(function() {
    document.querySelector("#ajax-call").addEventListener("click", event => {
        event.preventDefault();
        let formData = new FormData();
        formData.append('a', document.querySelector("#a").value);
        formData.append('b', document.querySelector("#b").value);
        let csrfTokenValue = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const request = new Request('{% url "compute" %}', {
            method: 'POST',
            body: formData,
            headers: {'X-CSRFToken': csrfTokenValue}
        });
        fetch(request)
            .then(response => response.json())
            .then(result => {
                const resultElement = document.querySelector("#ajax");
                resultElement.innerHTML = result["operation_result"];
            });
    });
});