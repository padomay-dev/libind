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

    //비밀번호 길이 및 일치여부 체크
    if (old_pass.value.length < 8) {
        old_pass.focus();
        password_old_result.innerHTML = "Old Password를 8글자 이상 입력해주세요"
        return false;
    }
    else if (new_pass1.value.length < 8) {
        new_pass1.focus()
        password_old_result.innerHTML = ""
        password_new1_result.innerHTML = "New Password를 8글자 이상 입력해주세요"
        return false;
    }
    else if (new_pass2.value.length < 8) {
        new_pass2.focus()
        password_new1_result.innerHTML = ""
        password_new2_result.innerHTML = "New Password Check를 8글자 이상 입력해주세요"
        return false;
    }
    else if (new_pass1.value != new_pass2.value) { //새로 입력한 패스워드 체크
        new_pass2.focus()
        password_new2_result.innerHTML = ""
        password_new2_result.innerHTML = "패스워드가 일치하지 않습니다."
        return false;
    }
    else if (old_pass.value == new_pass1.value) {
        new_pass1.focus()
        password_new2_result.innerHTML = ""
        password_old_result.innerHTML = "기존의 패스워드와 동일합니다."
        return false;
    }

    return true;
}