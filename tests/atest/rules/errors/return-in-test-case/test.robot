*** Test Case ***
Test with RETURN
    RETURN
    FOR    ${var}  IN RANGE  5
        RETURN
    END
    IF    $condition
        RETURN
    END
    IF    $condition    RETURN
    WHILE    $condition
        RETURN
    END
    TRY
        RETURN
    EXCEPT
        RETURN
    ELSE
        RETURN
    FINALLY
        RETURN
    END

*** Keywords ***
Keyword with RETURN
    RETURN
