package com.example.demo.config;

import org.apache.activemq.ActiveMQConnectionFactory;
import org.apache.activemq.jms.pool.PooledConnectionFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.jms.annotation.EnableJms;
import org.springframework.jms.config.DefaultJmsListenerContainerFactory;
import org.springframework.jms.core.JmsTemplate;

import com.example.demo.Receiver;
import com.example.demo.Sender;

@EnableJms
@Configuration
public class JmsConfiguration {
	
	@Value("${activemq.broker-url}")
	private String brokerUrl;
	@Value("${activemq.username}")
	private String userName;
	@Value("${activemq.password}")
	private String password;

	@Bean
	public ActiveMQConnectionFactory activeMQConnectionFactory() {
		ActiveMQConnectionFactory activeMQConnectionFactory = new ActiveMQConnectionFactory();
		activeMQConnectionFactory.setBrokerURL(brokerUrl);
		activeMQConnectionFactory.setUserName(userName);
		activeMQConnectionFactory.setPassword(password);

		return activeMQConnectionFactory;
	}
	
	@Bean
	@Autowired
	public PooledConnectionFactory pooledConnectionFactory(ActiveMQConnectionFactory activeMQConnectionFactory) {
		PooledConnectionFactory pooledConnectionFactory = new PooledConnectionFactory();
		pooledConnectionFactory.setConnectionFactory(activeMQConnectionFactory);
		pooledConnectionFactory.setMaxConnections(10);
		
		return pooledConnectionFactory;
	}

	@Bean
	@Autowired
	public DefaultJmsListenerContainerFactory jmsListenerContainerFactory(PooledConnectionFactory pooledConnectionFactory) {
		DefaultJmsListenerContainerFactory factory = new DefaultJmsListenerContainerFactory();
		factory.setConnectionFactory(pooledConnectionFactory);
		factory.setConcurrency("3-10");
		
		return factory;
	}
	
	@Bean
	@Autowired
	public JmsTemplate jmsTemplate(PooledConnectionFactory pooledConnectionFactory) {
		return new JmsTemplate(pooledConnectionFactory);
	}

	@Bean
	public Sender sender() {
		return new Sender();
	}
	
	
	@Bean
	public Receiver receiver() {
		return new Receiver();
	}
}
