package com.learn.microservices.limitsservice.configuration;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

@Component
@ConfigurationProperties("limits-service")
public class Configuration {

	private int minimum;
	private int maximum;

	
	
	public Configuration(int minimum, int maximum) {
		super();
		this.minimum = minimum;
		this.maximum = maximum;
	}
	public Configuration() {
		
	}
	/**
	 * @return the minimum
	 */
	public int getMinimum() {
		return minimum;
	}
	/**
	 * @param minimum the minimum to set
	 */
	public void setMinimum(int minimum) {
		this.minimum = minimum;
	}
	/**
	 * @return the maximum
	 */
	public int getMaximum() {
		return maximum;
	}
	/**
	 * @param maximum the maximum to set
	 */
	public void setMaximum(int maximum) {
		this.maximum = maximum;
	}
	
	
}
