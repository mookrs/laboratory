for a = 1:365
    filename = sprintf('%d.txt',a);
    fid = fopen(filename,'wt');
    sst = double(data(:,:,a));
    [m, n] = size(sst);
    for i = 1:m
        for j = 1:n
            if j == n
                fprintf(fid, '%g\n', sst(i, j));
            else
                fprintf(fid, '%g\t', sst(i, j));
            end
        end
    end
    fclose(fid);
end