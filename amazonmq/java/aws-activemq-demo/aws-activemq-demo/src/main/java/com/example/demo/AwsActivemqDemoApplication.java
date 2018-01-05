package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class AwsActivemqDemoApplication implements CommandLineRunner {
	
	@Autowired
	private Sender sender;

	public static void main(String[] args) {
		SpringApplication.run(AwsActivemqDemoApplication.class, args);
	}

	@Override
	public void run(String... args) throws Exception {
		String destination = "foo.bar";
		String message = "jms test";
		sender.send(destination, message);
	}
}
