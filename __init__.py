
from typing import Callable, Dict, List, Tuple, Type, TypeVar
from dataclasses import dataclass

@dataclass(frozen=True)
class Event: pass

E = Event
T = Type[E]
H = Callable[[E], None]

_handlers: Dict[T, List[H]] = {}

def dispatch_event(event: E) -> None:
    hs = _handlers.get(event.__class__)
    if hs:
        for h in hs: h(event)

def event_handler(*ts: Tuple[T]) -> Callable[[H], H]:
    def add(h: H) -> H:
        for t in ts:
            _handlers.setdefault(t, []).append(h)
        return h
    return add
