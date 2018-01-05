package com.example.demo;

import java.util.concurrent.CountDownLatch;

import org.springframework.jms.annotation.JmsListener;

import lombok.Getter;
import lombok.extern.slf4j.Slf4j;

@Slf4j
public class Receiver {
	
	@Getter
	private CountDownLatch latch = new CountDownLatch(1);

	@JmsListener(destination = "${activemq.queue.foo.bar}")
	public void receive(String message) {
		log.info("received message='{}'", message);
		latch.countDown();
	}
}
