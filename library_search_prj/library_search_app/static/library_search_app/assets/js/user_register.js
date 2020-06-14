function idCheck() {
    var id_result = document.getElementById("id_result");
    var user_id = document.getElementById("user_id");

    // ID길이 체크
    if (user_id.value.length < 4) {
        user_id.classList.remove("right_input");
        user_id.classList.add("worng_input");
        id_result.setAttribute("class", "text-danger");
        id_result.innerHTML = "ID의 길이는 4글자 이상입니다.";
        return false;
    } else {
        user_id.classList.remove("worng_input");
        id_result.setAttribute("class", "");
        id_result.innerHTML = "";
    }

    return_check = false;

    //ID중복체크
    $.ajax({
        type: "POST",
        url: "/library_search/user_register_idcheck/",
        async: false,
        data: {
            'user_id': $('#user_id').val(),
            'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
        },
        datatype: 'json',
        success: function (response) {
            if (response['overlap'] == 'fail') {
                user_id.classList.remove("right_input");
                user_id.classList.add("worng_input");
                id_result.setAttribute("class", "text-danger");
                id_result.innerHTML = "이미 존재하는 ID입니다";
                return_check = false;
            } else {
                user_id.classList.remove('worng_input')
                user_id.classList.add('right_input');
                id_result.setAttribute("class", "text-success");
                id_result.innerHTML = "사용 가능한 ID입니다";
                return_check = true;
            }
        },
    });

    return return_check;
}

function passwordLengthCheck() {
    var password = document.getElementById("password");
    var password_result = document.getElementById("password_result");

    //PASSWORd 길이체크
    if (password.value.length < 8) {
        password.classList.remove("right_input");
        password.classList.add("worng_input");
        password_result.setAttribute("class", "text-danger");
        password_result.innerHTML = "비밀번호는 8자리 이상이여야 합니다.;"
        return false;
    } else {
        password.classList.remove("worng_input");
        password.classList.add("right_input");
        password_result.setAttribute("class", "");
        password_result.innerHTML = "";
        return true;
    }
}

function passwordCheck() {
    var password = document.getElementById("password");
    var password_check = document.getElementById("password_check");
    var password_check_result = document.getElementById("password_check_result")

    //password 일치여부 판단.
    if (password.value == password_check.value) {
        password_check.classList.remove("worng_input")
        password_check.classList.add("right_input")
        password_check_result.setAttribute("class", "text-success");
        password_check_result.innerHTML = "페드워드가 일치합니다."
        return true;
    } else {
        password_check.classList.remove("right_input")
        password_check.classList.add("worng_input")
        password_check_result.setAttribute("class", "text-danger");
        password_check_result.innerHTML = "페드워드가 일치하지 않습니다.";
        return false;
    }
}

function emailCheck() {
    var email = document.getElementById("email");
    var email_result = document.getElementById("email_result");

    // //email 길이체크
    // if (email.value.length < 8) {
    //     email.classList.remove("right_input");
    //     email.classList.add("worng_input");
    //     email_result.setAttribute("class", "text-danger");
    //     email_result.innerHTML = "Email은 8자리 이상이여야 합니다.;"
    //     return false;
    // } else {
    //     email.classList.remove("worng_input");
    //     email.classList.add("right_input");
    //     email_result.setAttribute("class", "");
    //     email_result.innerHTML = ""
    // }
    //email형식체크
    var reg_email = /^([0-9a-zA-Z_\.-]+)@([0-9a-zA-Z_-]+)(\.[0-9a-zA-Z_-]+){1,2}$/;
    if (!reg_email.test(email.value)) {
        email.classList.remove("right_input");
        email.classList.add("worng_input");
        email_result.setAttribute("class", "text-danger");
        email_result.innerHTML = "올바른 email 형식이 아닙니다."
        return false;
    } else {
        email.classList.remove("worng_input");
        email.classList.add("right_input");
        email_result.setAttribute("class", "");
        email_result.innerHTML = ""
        return true;
    }
}

function nameCheck() {
    var name = document.getElementById("last_name");
    var name_result = document.getElementById("name_result");

    if (name.value.length < 2) {
        name.classList.remove("right_input");
        name.classList.add("worng_input");
        name_result.setAttribute("class", "text-danger");
        name_result.innerHTML = "이름은 2자리 이상이여야 합니다.;"
        return false;
    } else {
        name.classList.remove("worng_input");
        name.classList.add("right_input");
        name_result.setAttribute("class", "");
        name_result.innerHTML = ""
        return true;
    }
}

function checkField() {
    if (!idCheck()) {
        document.getElementById("user_id").focus();
        return false;
    } else if (!passwordLengthCheck()) {
        document.getElementById("password").focus();
        return false;
    } else if (!passwordCheck()) {
        document.getElementById("password_check").focus();
        return false;
    } else if (!emailCheck()) {
        document.getElementById("email").focus();
        return false;
    } else if (!nameCheck()) {
        document.getElementById("last_name").focus();
        return false;
    }

    return true;
}