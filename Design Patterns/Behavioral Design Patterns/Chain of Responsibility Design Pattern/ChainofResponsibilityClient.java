abstract class Logger{
    static int OUTPUTINFO = 1;
    static int ERRORINFO = 2;
    static int DEBUGINFO = 3;
    protected int levels;
    Logger nextLevelLogger;
    public void setNextLevelLogger(Logger nextLevelLogger) {
        this.nextLevelLogger = nextLevelLogger;
    }
    public void logMessage(int levels, String msg){
        if(this.levels <= levels){
            displayLogInfo(msg);
        }
        if(this.nextLevelLogger != null){
            this.nextLevelLogger.logMessage(levels, msg);
        }
    }
    protected abstract void displayLogInfo(String msg);
}

class ConsoleBasedLogger extends Logger{
    public ConsoleBasedLogger(int levels){
        this.levels = levels;
    }

    @Override
    protected void displayLogInfo(String msg) {
        System.out.println("ConsoleBasedLogger : "+ msg);
    }
}

class ErrorBasedLogger extends Logger{
    public ErrorBasedLogger(int levels){
        this.levels = levels;
    }

    @Override
    protected void displayLogInfo(String msg) {
        System.out.println("ErrorBasedLogger : "+ msg);
    }
}

class DebugBasedLogger extends Logger{
    public DebugBasedLogger(int levels) {
        this.levels = levels;
    }

    @Override
    protected void displayLogInfo(String msg) {
        System.out.println("DebugBasedLogger : "+ msg);
    }
}

public class ChainofResponsibilityClient{
    private static Logger doChaining(){
        Logger consoleLogger = new ConsoleBasedLogger(Logger.OUTPUTINFO);

        Logger errorLogger = new ErrorBasedLogger(Logger.ERRORINFO);
        consoleLogger.setNextLevelLogger(errorLogger);

        Logger debugLogger = new DebugBasedLogger(Logger.DEBUGINFO);
        errorLogger.setNextLevelLogger(debugLogger);

        return consoleLogger;
    }
    public static void main(String[] args) {
        Logger chainLogger = doChaining();
        chainLogger.logMessage(Logger.OUTPUTINFO, "Enter sequence of values");
        chainLogger.logMessage(Logger.ERRORINFO, "An error occured now");
        chainLogger.logMessage(Logger.DEBUGINFO, "This was error now. Debugging completed");
    }
}
