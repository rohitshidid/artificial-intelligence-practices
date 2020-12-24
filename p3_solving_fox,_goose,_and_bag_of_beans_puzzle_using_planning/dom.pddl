(define (domain dom)

    (:predicates (onLeft ?x))

    (:action cross
        :parameters (?x)
        :precondition   (or 
                            (and ; farmer can pass if goose and fox are not at the same side and beans and goose are not at the same side
                                (= farmer ?x)
                                (and
                                    (or ;goose and fox are not at the same side
                                        (and
                                            (onLeft goose)
                                            (not(onLeft fox))
                                        )
                                        (and
                                            (onLeft fox)
                                            (not(onLeft goose))
                                        )
                                    )
                                    (or ;goose and beans are not at the same side
                                        (and
                                            (onLeft beans)
                                            (not(onLeft goose))
                                        )
                                        (and
                                            (onLeft goose)
                                            (not(onLeft beans))
                                        )
                                    )
                                ) 
                            )
                            (and ;(x and farmer at the same side) (x == fox or x == beans) and 
                                (or ;x has to be at the same side with farmer in order to pass
                                    (and 
                                        (onLeft farmer)
                                        (onLeft ?x)
                                    )
                                    (and 
                                        (not(onLeft farmer))
                                        (not(onLeft ?x))
                                    )
                                )
                                (or
                                    (= goose ?x) ;goose can pass with the farmer without any precondition
                                    (and ;if x is beans
                                        (= beans ?x)
                                        (or 
                                            (and
                                                (onLeft fox)
                                                (not(onLeft goose))
                                            )
                                            (and
                                                (onLeft goose)
                                                (not(onLeft fox))
                                            )
                                        )
                                    )
                                    (and ;if x is fox
                                        (= fox ?x)
                                        (or 
                                            (and
                                                (onLeft beans)
                                                (not(onLeft goose))
                                            )
                                            (and
                                                (onLeft goose)
                                                (not(onLeft beans))
                                            )
                                        )
                                    )
                                ) 
                            )     
                        )
        :effect 
            (and
                (when (onLeft farmer) (not(onLeft farmer))) 
                (when (not(onLeft farmer)) (onLeft farmer)) 
                (when (onLeft ?x) (not (onLeft ?x)))  
                (when (not (onLeft ?x)) (onLeft ?x)) 
            )
    )
)



