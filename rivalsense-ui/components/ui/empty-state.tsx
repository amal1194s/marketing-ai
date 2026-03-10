import { LucideIcon } from "lucide-react";
import { Button } from "./button";
import { Card, CardContent } from "./card";

interface EmptyStateProps {
  icon: LucideIcon;
  title: string;
  description: string;
  action?: {
    label: string;
    onClick: () => void;
  };
}

export function EmptyState({ icon: Icon, title, description, action }: EmptyStateProps) {
  return (
    <Card className="border-2 border-dashed border-border/50 hover:border-primary/30 transition-all duration-300 bg-accent/10">
      <CardContent className="flex flex-col items-center justify-center py-16 px-6">
        <div className="flex h-20 w-20 items-center justify-center rounded-2xl bg-accent/50 border-2 border-border/30 mb-6 group-hover:scale-105 transition-transform">
          <Icon className="h-10 w-10 text-muted-foreground" />
        </div>
        <h3 className="text-xl font-bold mb-2 text-center">{title}</h3>
        <p className="text-sm text-muted-foreground mb-8 text-center max-w-md leading-relaxed">
          {description}
        </p>
        {action && (
          <Button onClick={action.onClick} size="lg" className="gap-2">
            <Icon className="h-4 w-4" />
            {action.label}
          </Button>
        )}
      </CardContent>
    </Card>
  );
}
