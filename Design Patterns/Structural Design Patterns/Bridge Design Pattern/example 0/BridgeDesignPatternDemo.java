import java.util.List;
import java.util.ArrayList;

interface Question{
    void nextQuestion();
    void previousQuestion();
    void newQuestion(String question);
    void deleteQuestion(String question);
    void displayQuestion();
    void displayAllQuestion();
}

class JavaQuestions implements Question{
    private int current = 0;
    private List<String> questions = new ArrayList<>();

    JavaQuestions(){
        questions.add("What is class?");
        questions.add("What is interface?");
    }

    @Override
    public void nextQuestion() {
        if(current < questions.size()){
            current++;
            System.out.println(current);
        }
    }

    @Override
    public void previousQuestion() {
       if(current > 0){
          current--; 
       }
    }

    @Override
    public void newQuestion(String question) {
        questions.add(question);
    }

    @Override
    public void deleteQuestion(String question) {
        questions.remove(question);
    }

    @Override
    public void displayQuestion() {
        System.out.println(questions.get(current));
    }

    @Override
    public void displayAllQuestion() {
       for(String question : questions){
           System.out.println(question);
       }
    }
}


class QuestionManager{
    protected Question q;
    public String catalog;

    public QuestionManager(String catalog){
        this.catalog = catalog;
    }

    public void next(){
        q.nextQuestion();
    }

    public void previous(){
        q.previousQuestion();
    }

    public void newOne(String question){
        q.newQuestion(question);
    }

    public void delete(String question){
        q.deleteQuestion(question);
    }

    public void display(){
        q.displayQuestion();
    }

    public void displayAll(){
        System.out.println("Question paper: " + catalog);
        q.displayAllQuestion();
    }
}

class QuestionFormat extends QuestionManager{

    public QuestionFormat(String catalog) {
        super(catalog);
    }

    public void displayAll(){
        System.out.println("--------------------");
        super.displayAll();
        System.out.println("--------------------");
    }
}
public class BridgeDesignPatternDemo{
    public static void main(String[] args) {
        QuestionFormat questions = new QuestionFormat("Java programming languages");

        questions.q = new JavaQuestions();
        questions.newOne("What is inheritance? ");

        questions.newOne("How many types of inheritance are there in Java?");
        questions.displayAll();
    }
}