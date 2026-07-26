// =============================
// Street Light Tracker
// script.js
// =============================

// Today's Date Automatically
window.onload = function () {

    let date = document.querySelector("input[name='reported_date']");

    if (date) {

        let today = new Date().toISOString().split("T")[0];

        date.value = today;

    }

}


// =============================
// Form Validation
// =============================

function validateForm() {

    let pole = document.getElementsByName("pole_id")[0].value.trim();

    let ward = document.getElementsByName("ward")[0].value.trim();

    let street = document.getElementsByName("street")[0].value.trim();

    if (pole == "") {

        alert("Pole ID is Required");

        return false;

    }

    if (ward == "") {

        alert("Ward is Required");

        return false;

    }

    if (street == "") {

        alert("Street Name is Required");

        return false;

    }

    return true;

}


// =============================
// Delete Confirmation
// =============================

function confirmDelete() {

    return confirm("Are you sure you want to delete this complaint?");

}


// =============================
// Search Validation
// =============================

function validateSearch() {

    let search = document.getElementById("search");

    if (search) {

        if (search.value.trim() == "") {

            alert("Enter Pole ID, Ward or Street");

            search.focus();

            return false;

        }

    }

    return true;

}


// =============================
// Success Notification
// =============================

function successMessage(msg) {

    alert(msg);

}


// =============================
// Reset Form
// =============================

function clearForm() {

    document.querySelector("form").reset();

}


// =============================
// Search Filter
// =============================

function filterTable() {

    let input = document.getElementById("search");

    let filter = input.value.toUpperCase();

    let table = document.getElementById("complaintTable");

    let tr = table.getElementsByTagName("tr");

    for (let i = 1; i < tr.length; i++) {

        let td1 = tr[i].getElementsByTagName("td")[1];
        let td2 = tr[i].getElementsByTagName("td")[2];
        let td3 = tr[i].getElementsByTagName("td")[3];

        if (td1 || td2 || td3) {

            let txt1 = td1.textContent || td1.innerText;
            let txt2 = td2.textContent || td2.innerText;
            let txt3 = td3.textContent || td3.innerText;

            if (
                txt1.toUpperCase().indexOf(filter) > -1 ||
                txt2.toUpperCase().indexOf(filter) > -1 ||
                txt3.toUpperCase().indexOf(filter) > -1
            ) {

                tr[i].style.display = "";

            }

            else {

                tr[i].style.display = "none";

            }

        }

    }

}