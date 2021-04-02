var 
    F: Text;
    A: Array[0..200] of Integer;
    I, J, K, L: Integer; 

begin
    Assign(F, '01-input.txt');
    Reset(F);

    I := -1;
    while not EOF(F) do begin
        if not SeekEOLN(F) then begin
            Inc(I);
            Readln(F, A[I]);
        end
    end;
    for J := 0 to I do begin
        for K := J + 1 to I do
            if 2020 - A[J] = A[K] then
            begin
                write(A[J] * A[K]);
                writeln;
            end
    end;
    for J := 0 to I do begin
        for K := J + 1 to I do
            for L := K + 1 to I do
                if 2020 - A[K] - A[L] = A[J] then
                begin
                    write(A[J] * A[K] * A[L]);
                    writeln;
                end
    end;
    close(F);
end.

    
