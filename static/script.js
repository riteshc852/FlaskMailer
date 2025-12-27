 const form = document.getElementById("contactForm");
 const submit_btn = document.querySelector(".submit-btn");
  form.addEventListener("submit", async (e) => {
    e.preventDefault(); // stop page reload
    submit_btn.textContent = "Wait a moment...";
    submit_btn.disabled = true;
    submit_btn.classList.add("btn-toggle");
    
    const formData = new FormData(form);

    try {
      const res = await fetch("/", {
        method: "POST",
        body: formData
      });
      const data = await res.json();
      if (data.status === "success") {
        alert("Email sent successfully!");
        submit_btn.innerText = "Send Your Message"; 
        form.reset();
      }
      else {
        alert("Failed to send email");
      }

    } 
    catch (err) {
      alert("Server error");
    }
    submit_btn.textContent = "Send";
    submit_btn.disabled = false;
    submit_btn.classList.remove("btn-toggle");
  });
