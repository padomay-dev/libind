// //Input이 비었는지 안비었는지 체크하는 js
// (function () {
//     'use strict';
//     window.addEventListener('load', function () {
//         // Get the forms we want to add validation styles to
//         var forms = document.getElementsByClassName('needs-validation');
//         // Loop over them and prevent submission
//         var validation = Array.prototype.filter.call(forms, function (form) {
//             form.addEventListener('submit', function (event) {
//                 if (form.checkValidity() === false) {
//                     event.preventDefault();
//                     event.stopPropagation();
//                 }
//                 form.classList.add('was-validated');
//             }, false);
//         });
//     }, false);
// })();

function password_check() {
    old_pass = document.getElementById("id_old_password")
    new_pass1 = document.getElementById('id_new_password1');
    new_pass2 = document.getElementById('id_new_password2');
    password_old_result = document.getElementById('password_old_result');
    password_new1_result = document.getElementById('password_new1_result');
    password_new2_result = document.getElementById('password_new2_result');

    //비밀 번호 빈칸 및 일치여부 체크
    if (old_pass.value.length < 8) {
        old_pass.focus();
        password_new1_result.style.display = "none"
        password_new2_result.style.display = "none"
        password_old_result.style.display = "block";
        return false;
    } else if (new_pass1.value.length < 8) {
        new_pass1.focus()
        password_old_result.style.display = "none"
        password_new2_result.style.display = "none"
        password_new1_result.style.display = "block";
        return false;
    } else if (new_pass2.value.length < 8) {
        new_pass2.focus()
        password_old_result.style.display = "none"
        password_new1_result.style.display = "none"
        password_new2_result.style.display = "block";
        return false;
    } else if (new_pass1.value != new_pass2.value) {
        new_pass2.focus()
        password_new2_result.innerHTML = "패스워드가 일치하지 않습니다."
        password_new2_result.style.display = "block";
        return false;
    }

    return true;
}