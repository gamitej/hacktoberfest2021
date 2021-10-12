package com.learn.microservices.currencyconversion.proxy;

import java.math.BigDecimal;

import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

import com.learn.microservices.currencyconversion.model.CurrencyConversion;

//@FeignClient(name="currency-exchange",url="localhost:8000")
@FeignClient(name="zuul-api-gateway")
public interface CurrencyExchangeProxy {

//	@GetMapping("currency-exchange/from/{from}/to/{to}")
	@GetMapping("/currency-exchange/currency-exchange/from/{from}/to/{to}")
	public CurrencyConversion calculateCurrencyConversion(
			@PathVariable String from,
			@PathVariable String to);
	
	
		
}
