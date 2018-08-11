

struct Link
    fr :: Any
    to :: Any
    flag :: Int

    Link(fr, to) = new(fr, to, Int)
end

abstract type AbstractNode end


struct Scalar{T} <: AbstractNode
    name  :: AbstractString
end

struct Field{T} <: AbstractNode
    name  :: AbstractString
    dims  ::
end

struct Operator <: AbstractNode
    name  :: 
end


struct Variable <: AbstractNode
    links :: Array{Link, 1}
    name  :: AbstractString
    desc  :: AbstractString

    Variable(n) = new(Array{Link,1}(n), "", "")
end






