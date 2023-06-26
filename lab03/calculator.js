class Calculator{

    constructor(){
        this.operands = []
    }
    
    add(num1, num2){
        this.operands[0] = (num1 + num2);
    }
    
    multiply(num1, num2){
        this.operands[0] = (num1 * num2);
    }
    
    subtract(num1, num2){
        this.operands[0] = (num1 - num2);
    }
    
    divide(num1, num2){
        this.operands[0] = (num1 / num2);
    }
    
    pow(num1, num2){
        this.operands[0] = (num1 ** num2);
    }
    
    squareRoot(num){
        this.operands[0] = (Math.sqrt(num));
        console.log(this.operands[0]);
    }
    
    sin(num){
        this.operands[0] = Math.sin(num);
    }
    
    cos(num){
        this.operands[0] = Math.cos(num);
    }
    
    tan(num){
        this.operands[0] = Math.tan(num);
    }

    clear(){
        this.operands = []
    }
    
    operate(operator){
        if (this.operands.length == 2){
            switch (operator){
                case "+":
                    this.add(this.operands[0], this.operands[1]);
                    break;
                case "-":
                    this.subtract(this.operands[0], this.operands[1]);
                    break;
                case "*":
                    this.multiply(this.operands[0], this.operands[1]);
                    break;
                case "/":
                    this.divide(this.operands[0], this.operands[1]);
                    break;
                case "pow":
                    this.pow(this.operands[0], this.operands[1]);
                    break;
                case "sqrt":
                    this.squareRoot(this.operands[0]);
                    break;
                case "sin":
                    this.sin(this.operands[0]);
                    break;
                case "cos":
                    this.cos(this.operands[0]);
                    break;
                case "tan":
                    this.tan(this.operands[0]);
                    break;
            }
                this.operands.pop();
        }
            return this.operands[this.operands.length - 1];
        }
    }


function screenController(){
    const calculator = new Calculator();
    let pickedOperator;
    let isFirstClick = true;

    const display = document.querySelector(".display");
    const numbers = document.querySelectorAll(".num");

    numbers.forEach((number) => {
        number.addEventListener("click", () =>{
            displayNums = display.textContent;
            if (isFirstClick){
                displayNums = "";
                isFirstClick = false;
            } 
            display.textContent = displayNums + number.textContent;
        });
    });
    

    const operators = document.querySelectorAll(".operator");
    operators.forEach((operator) => {
        operator.addEventListener("click", () => {
            if (operator.textContent === "sin" || operator.textContent === "cos" || operator.textContent === "tan"){
                pickedOperator = operator.textContent;
            }
            
            calculator.operands.push(parseFloat(display.textContent));
            isFirstClick = true;
            
            display.textContent = calculator.operate(pickedOperator);
            pickedOperator = operator.textContent;

            if (operator.textContent == "AC"){
                calculator.clear();
                display.textContent = "0";
            }

        });
    });

}
screenController();