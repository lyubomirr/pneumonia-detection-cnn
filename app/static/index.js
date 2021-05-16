$(document).ready(() => {
    $("#pic").change(event => {
        var image = document.getElementById('output');
        image.src = URL.createObjectURL(event.target.files[0]);
    });

    $("#pic-form").submit((e) => {
        e.preventDefault();

        $("#response").css("display", "none");
        $(".loader").css("display", "block")

        var file = $("#pic")[0].files[0]
        var formData = new FormData();
        formData.append("pic", file)

        fetch("/submit", {
                method: "post",
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                $("#condition").text(data.class);
                $("#confidence").text(Math.round(data.confidence * 100) / 100 + "%");

                $(".loader").css("display", "none")
                $("#response").css("display", "block");
            });
    });
});