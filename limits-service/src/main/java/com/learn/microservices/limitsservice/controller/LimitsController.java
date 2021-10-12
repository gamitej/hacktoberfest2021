package com.learn.microservices.limitsservice.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.learn.microservices.limitsservice.configuration.Configuration;
import com.learn.microservices.limitsservice.model.Limits;

@RestController
public class LimitsController {

	@Autowired
	Configuration configuration;
	
	@GetMapping("/")
	public Limits retrieveLimits() {
		return new Limits(configuration.getMinimum(),configuration.getMaximum());
	}
}
