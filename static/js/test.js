function check() { 

    var q1 = document.quiz.q1.value
    var q2 = document.quiz.q2.value
    var q3 = document.quiz.q3.value
    var q4 = document.quiz.q4.value
    var q5 = document.quiz.q5.value
    var q6 = document.quiz.q6.value

    var correct = 0;

    var flag = 1;

    if (q1 == "2") {
        correct++;
    }
    else if (q1 == "") {
        flag = 0;
    }

    if (q2 == "-1") {
        correct++;
    }
    else if (q2 == "") {
        flag = 0;
    }

    if (q3 == "1") {
        correct++;
    }
    else if (q3 == "") {
        flag = 0;
    }

    if (q4 == "1") {
        correct++;
    }
    else if (q4 == "") {
        flag = 0;
    }

    if (q5 == "60°") {
        correct++;
    }
    else if (q5 == "") {
        flag = 0;
    }

    if (q6 == "-5") {
        correct++;
    }
    else if (q6 == "") {
        flag = 0;
    }

    if (flag == 0) {
        return false;
    }
    else {
        if (correct > 2) {
            alert("Оценката ви е: " + correct);;
        }
        else {
            alert("Оценката ви е: 2");
        }
    }

}