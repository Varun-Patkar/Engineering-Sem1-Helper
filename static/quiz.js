const questions =[
    {
        q:'Enter question 1',
        options:['option 1', 'option 2','option 3','option 4'],
        answer:0
    },
    {
        q:'Enter question 2',
        options:['option 1', 'option 2','option 3','option 4'],
        answer:1
    },
    {
        q:'Enter question 3',
        options:['option 1', 'option 2','option 3','option 4'],
        answer:2
    },
    {
        q:'Enter question 4',
        options:['option 1', 'option 2','option 3','option 4'],
        answer:3
    },
    {
        q:'Enter question 5',
        options:['option 1', 'option 2','option 3','option 4'],
        answer:1
    }
]
const options=document.querySelector(".options").children;
const answerTrackerContainer=document.querySelector(".answer-tracker");
const correctAnswerSpan=document.querySelector(".correct-answers");
const totalAnswerSpan2=document.querySelector(".total-question2");
const percentage=document.querySelector(".percentage");
const questionNumberSpan=document.querySelector(".question-num-value");
const totalQuestionSpan=document.querySelector(".total-question");
const question=document.querySelector(".question");
const op1=document.querySelector(".option1");
const op2=document.querySelector(".option2");
const op3=document.querySelector(".option3");
const op4=document.querySelector(".option4");
let questionIndex;
let index=0;
let myArray=[];
let score=0;

//Question,options,answers



//set question,question number and options
totalQuestionSpan.innerHTML=questions.length;
function load(){
   questionNumberSpan.innerHTML=index+1;
   question.innerHTML=questions[questionIndex].q;
   op1.innerHTML=questions[questionIndex].options[0];
   op2.innerHTML=questions[questionIndex].options[1];
   op3.innerHTML=questions[questionIndex].options[2];
   op4.innerHTML=questions[questionIndex].options[3];
   index++;
}

function check(element){
    if(element.id==questions[questionIndex].answer){
        //console.log("correct")
        element.classList.add("correct");
        updateAnswerTracker("correct");
        score++;
    }
    else{
        //console.log("wrong")
        element.classList.add("wrong");
        updateAnswerTracker("wrong");
    }
    disabledOptions()
}

function disabledOptions(){
    for(let i=0; i<options.length; i++){
        options[i].classList.add("disabled");
        if(options[i].id==questions[questionIndex].answer){
          options[i].classList.add("correct");    
        }
    }
}

function enabledOptions(){
    for(let i=0; i<options.length; i++){
        options[i].classList.remove("disabled","correct","wrong");
    }
}


function answerTracker(){
    for (let i = 1; i <= questions.length; i++) {
        const div = document.createElement("div");
        var textHere= document.createTextNode(i);
        answerTrackerContainer.appendChild(div);
        div.appendChild(textHere);       
    }
}

function updateAnswerTracker(classNam){
    answerTrackerContainer.children[index-1].classList.add(classNam);
}

function validate(){
    if(!options[0].classList.contains("disabled")){
        alert("Please select one option");
    }
    else{
        enabledOptions();
        randomQuestion();
    }
}

function next(){
    validate();
}

function randomQuestion(){
    let randomNumber = Math.floor(Math.random()*questions.length);
    let hitDuplicate=0;
    if(index==questions.length){
        quizOver();
    }
    else{
        if(myArray.length>0){
            for (let i = 0; i < myArray.length; i++) {
                if (myArray[i]==randomNumber) {
                    hitDuplicate=1;
                    break;
                } 
            }
            if(hitDuplicate==1){
                randomQuestion();
            }
            else{
                questionIndex=randomNumber;
                load();
            }
        }
        if(myArray.length==0){
            questionIndex=randomNumber;
            load();
         }
    
    myArray.push(randomNumber)
    //console.log("myArray:"+myArray);
    
    }
}

function quizOver(){
    document.querySelector(".quiz-over").classList.add("show");
    correctAnswerSpan.innerHTML=score;
    totalAnswerSpan2.innerHTML=questions.length;
    percentage.innerHTML=(score/questions.length)*100 + "%";

}

function tryAgain()
{
    window.location.reload();
}
window.onload=function(){
    randomQuestion();
    answerTracker();
}