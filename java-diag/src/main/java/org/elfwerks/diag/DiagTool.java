package org.elfwerks.diag;

import org.apache.commons.cli.BasicParser;
import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.CommandLineParser;
import org.apache.commons.cli.Options;
import org.apache.commons.cli.ParseException;

public class DiagTool {

  public static CommandLine parseCommandLine(String[] args) throws ParseException {
    Options options = new Options();

    options.addOption("d", "daemon", false, "daemonize");

    CommandLineParser cmdLineParser = new BasicParser();
    CommandLine cmdLine = cmdLineParser.parse(options, args);
    return cmdLine;
  }


  public static void main(String[] args) throws Exception {
    CommandLine cmdLine = parseCommandLine(args);

    System.out.println("java.version: "+System.getProperties().getProperty("java.version"));

    if ( cmdLine.hasOption('d') ) {
        System.out.println("daemonizing, press ^C to exit...");
        while ( true ) {
            Thread.sleep(1000);
        }
    }

    System.out.println("[stdout] done.");
  }

}
