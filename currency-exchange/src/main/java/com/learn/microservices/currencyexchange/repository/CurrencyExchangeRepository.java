package com.learn.microservices.currencyexchange.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.learn.microservices.currencyexchange.model.CurrencyExchange;

public interface CurrencyExchangeRepository extends JpaRepository<CurrencyExchange, Long>{
	
	CurrencyExchange findByFromAndTo(String from,String to);

}
