(define (problem prob)
    (:domain dom)

    (:objects farmer fox goose beans) ;objects
    (:init 
         (onLeft farmer)
         (onLeft fox)
         (onLeft goose)
         (onLeft beans))
    
    (:goal (and (not (onLeft farmer))
                (not (onLeft fox))
                (not (onLeft goose))
                (not (onLeft beans))
            )
    )
)
