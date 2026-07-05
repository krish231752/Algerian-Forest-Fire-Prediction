document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("predictForm");
    
    if (form) {
        form.addEventListener("submit", function() {
            const btnText = document.getElementById("btnText");
            const btnSpinner = document.getElementById("btnSpinner");
            const submitBtn = document.getElementById("submitBtn");

            submitBtn.classList.add("disabled");
            
            btnText.innerText = "Processing...";
            btnSpinner.classList.remove("d-none");
        });
    }
});
