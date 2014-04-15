package org.elfwerks.diag;

import io.dropwizard.Application;
import io.dropwizard.setup.Bootstrap;
import io.dropwizard.setup.Environment;

public class DiagServletMain extends Application<DiagConfiguration>{

    public static void main(String[] args) throws Exception {
        new DiagServletMain().run(args);
    }

    @Override
    public String getName() {
        return "diag-servlet";
    }
    
    @Override
    public void initialize(Bootstrap<DiagConfiguration> bootstrap) {
        
    }
    
    @Override
    public void run(DiagConfiguration configuration, Environment environment) {
        
    }
    
}
